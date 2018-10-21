pipeline {
    agent { docker { image 'python:3.5.1' } }
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('sh') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('env') {
            steps {
                sh 'printenv'
            }
        }
        stage('timeouts and retry') {
            steps {
                retry(3) {
                    echo 'retry step from Timeouts and retry stage'
                }

                timeout(time: 3, unit: 'MINUTES') {
                    echo 'timeout step from Timeouts and retry stage'
                }
            }
        }
        stage('python') {
            steps {
                sh 'python3 ./app/hello.py'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}