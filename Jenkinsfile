pipeline {
    agent any

    stages {
        stage('1. Checkout') {
            steps {
                // Pull code from GitHub
                checkout scm
            }
        }

        stage('2. Test & Coverage') {
            steps {
                // Run JUnit tests and generate JaCoCo reports
                bat 'mvn clean test' 
            }
            post {
                always {
                    // Publish Unit Test results in Jenkins
                    junit '**/target/surefire-reports/*.xml' [cite: 352, 800]
                }
            }
        }

        stage('3. Docker Build') {
            steps {
                // Create a Docker image tagged with the build number
                bat 'docker build -t devops-final-app:%BUILD_NUMBER% .' [cite: 1152]
            }
        }

        stage('4. Deploy (Run)') {
            steps {
                // Stop and remove old container if it exists
                bat 'docker stop my-app || true'
                bat 'docker rm my-app || true'
                // Run the new container on port 5050
                bat 'docker run -d --name my-app -p 5050:8080 devops-final-app:%BUILD_NUMBER%' [cite: 39, 1070]
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! App is live at http://localhost:5050'
        }
        failure {
            echo 'Pipeline failed. Check the logs for errors.' [cite: 389, 841]
        }
    }
}
