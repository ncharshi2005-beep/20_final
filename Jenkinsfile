pipeline {
    agent any
    stages {
        stage('1. Checkout') {
            steps { checkout scm }
        }
        stage('2. Run Tests') {
            steps {
                // Runs the python test script
                bat 'python test_app.py'
            }
        }
        stage('3. Build Docker Image') {
            steps {
                // Build and tag with Jenkins build number
                bat 'docker build -t calc-web-app:%BUILD_NUMBER% .'
            }
        }
        stage('4. Deploy to Browser') {
            steps {
                // Remove old container if it exists
                bat 'docker stop my-calc-container || true'
                bat 'docker rm my-calc-container || true'
                // Run on port 5050 so it doesn't clash with Jenkins
                bat 'docker run -d --name my-calc-container -p 5050:8080 calc-web-app:%BUILD_NUMBER%'
            }
        }
    }
    post {
        success { echo 'App is live! Open http://localhost:5050' }
    }
}
