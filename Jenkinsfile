pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t calc-app .'
            }
        }

        stage('Run Calculator in Docker') {
            steps {
                bat 'docker run --rm calc-app'
            }
        }
    }
}
