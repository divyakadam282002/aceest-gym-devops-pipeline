pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Repository cloned successfully'
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                echo "Running CI pipeline..."
                '''
            }
        }

        stage('Simulate Dependency Installation') {
            steps {
                sh '''
                echo "Installing dependencies..."
                '''
            }
        }

        stage('Simulate Tests Execution') {
            steps {
                sh '''
                echo "Running pytest..."
                '''
            }
        }

        stage('Simulate Docker Build') {
            steps {
                sh '''
                echo "Docker build simulated successfully"
                '''
            }
        }

    }

    post {

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }

    }
}