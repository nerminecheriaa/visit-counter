pipeline {
    agent any

    environment {
        IMAGE_NAME = "nerminecheriaa22/counter-app"
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    triggers { githubPush() }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build & Unit Tests') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '-e HOME=/tmp'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    pip install --no-cache-dir -r requirements.txt pytest
                    python -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                 usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh '''
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                        docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }
    }

    post {
        always { sh 'docker logout || true' }
        success { echo "Image publiée : ${IMAGE_NAME}:${IMAGE_TAG}" }
        failure { echo "Pipeline en échec" }
    }
}