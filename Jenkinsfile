
pipeline {
    agent any

    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo 'Running Selenium Tests using pytest'

                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'

                // Start Flask app in background
                bat 'start /B python app.py > app.log 2>&1'

                // Wait for Flask to start
                bat 'ping 127.0.0.1 -n 6 > nul'

                // Run Selenium tests
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image'
                bat 'docker build -t seleniumdemoapp:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                    powershell -NoProfile -Command "$env:DOCKER_PASS | docker login -u $env:DOCKER_USER --password-stdin"
                    '''
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                bat 'docker tag seleniumdemoapp:v1 mudavathchandana/sample2026:seleniumtestimage'
                bat 'docker push mudavathchandana/sample2026:seleniumtestimage'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the Console Output.'
        }
    }
}
