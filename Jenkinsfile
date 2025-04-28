/* 1. Kavya Shivakumar (G01520934)
2. Sehaj Gill (G01535820)
3. Jaanaki Swaroop P(G01502869)
4. Koushik Vasa (G01480627) */

pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-cred')
    }
    stages {
        stage('Timestamping') {
            steps {
                script {
                    // Defining a build timestamp variable
                    env.BUILD_TIMESTAMP = new Date().format("yyyyMMddHHmmss", TimeZone.getTimeZone('UTC'))
                    echo "Build timestamp: ${env.BUILD_TIMESTAMP}"
                }
            }
        }

        stage('Building a Docker Image') {
            steps {
                script {
                    // Securely handling Docker login
                    withCredentials([usernamePassword(credentialsId: 'docker-cred', 
                                                      usernameVariable: 'DOCKER_USER', 
                                                      passwordVariable: 'DOCKER_PASS')]) {
                        sh """
                            echo "\$DOCKER_PASS" | docker login -u "\$DOCKER_USER" --password-stdin
                        """
                    }

                    def imageName = "jswaroop/swe-survey:${env.BUILD_TIMESTAMP}"
                    sh "docker build -t ${imageName} ."

                    env.IMAGE_NAME = imageName
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                script {
                    sh "docker push ${env.IMAGE_NAME}"
                }
            }
        }

        stage('Deploy to Rancher') {
            steps {
                script {
                    echo "Deploying to Kubernetes cluster: assignhome in namespace: assignment-namespace"

                    sh "kubectl config use-context assignhome"

                    sh "kubectl set image deployment/newpython container-0=${env.IMAGE_NAME} --namespace=test"

                    sh "kubectl rollout status deployment/newpython --namespace=test"
                }
            }
        }
    }
}
