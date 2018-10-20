pipeline {
    agent { 
        docker { 
            image 'python:3.5.1' 
            args '-u root:root'
        } 
    }
    stages {
        stage('build') {
            steps {
                sh 'id -a'
                sh 'python --version'
            }
        }
    }
}