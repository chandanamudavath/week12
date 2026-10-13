
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Chandana\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\python.exe'
        DOCKER_IMAGE = 'mudavathchandana/sample2026:seleniumtestimage'
    }

    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo 'Running Selenium Tests using pytest'

                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip install -r requirements.txt'

                // Start Flask application
                bat 'start "FlaskApp" /B "%PYTHON%" app.py'

                // Wait for Flask to start
                bat 'ping 127.0.0.1 -n 6 > nul'

                // Run Selenium tests
                bat '"%PYTHON%" -m pytest -v'
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
                bat 'docker tag seleniumdemoapp:v1 %DOCKER_IMAGE%'
                bat 'docker push %DOCKER_IMAGE%'
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
            echo 'Pipeline failed. Check the Jenkins Console Output.'
        }
    }
}
