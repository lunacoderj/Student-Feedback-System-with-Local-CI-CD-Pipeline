// Student Feedback System - Jenkins Declarative Pipeline

pipeline {
    agent any

    environment {
        IMAGE_NAME  = 'student-feedback-system'
        CONTAINER   = 'student-feedback-app'
        APP_PORT    = '5000'
    }

    stages {

        // ---- Stage 1: Source ----
        stage('Source') {
            steps {
                echo '📥 Pulling latest source code...'
                checkout scm
            }
        }

        // ---- Stage 2: Build ----
        stage('Build') {
            steps {
                echo '🔨 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        // ---- Stage 3: Test ----
        stage('Test') {
            steps {
                echo '🧪 Running smoke test...'
                sh """
                    docker run --rm ${IMAGE_NAME}:latest python -c \
                    "from app import app; print('[✓] Flask app imports OK')"
                """
            }
        }

        // ---- Stage 4: Deploy ----
        stage('Deploy') {
            steps {
                echo '🚀 Deploying with Ansible...'
                sh '''
                    cd ansible
                    ansible-playbook -i inventory deploy.yml --connection=local
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully! App running at http://localhost:5000'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs above for errors.'
        }
        always {
            echo '📋 Pipeline execution finished.'
        }
    }
}
