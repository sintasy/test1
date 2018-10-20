pipeline {
    agent { 
        docker { 
            image 'python:3.5.1' 
            args '-v $HOME/.m2:/root/.m2'
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