pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out project files..."
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t calc-app .'
            }
        }

        stage('Run Calculator in Docker') {
            steps {
                echo "Running calculator inside Docker..."
                sh 'docker run --rm calc-app'
            }
        }
    }
}
