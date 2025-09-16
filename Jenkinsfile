pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t calc-app .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm calc-app python test_calculator.py'
            }
        }

        stage('Run Calculator in Docker') {
            steps {
                bat 'docker run --rm calc-app'
            }
        }
    }
}
