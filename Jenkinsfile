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
                // Windows-friendly way to ignore errors if container doesn't exist
                bat 'docker stop my-calc-container >nul 2>&1 || ver >nul'
                bat 'docker rm my-calc-container >nul 2>&1 || ver >nul'
                
                // Deploying the new build
                bat 'docker run -d --name my-calc-container -p 5050:5020 calc-web-app:%BUILD_NUMBER%'
            }
        }
    }
    post {
        success { 
            echo "Build # ${env.BUILD_NUMBER} is live!"
            echo 'App is live! Open http://localhost:5050' 
        }
        failure {
            echo 'Deployment failed. Check the console logs.'
        }
    }
}
