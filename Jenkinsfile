pipeline {
    agent {
        label 'docker'  // Use an agent with Docker installed
    }

    stages {
        stage('Run Docker Build') {
            steps {
                script {
                    // Run a Docker container
                    sh "docker build -d 'python:3.8-slim' ."  // Example Docker build command
                }
            }
        }
    }

    stages {     
        stage('Checkout GitHub Repository') {
            steps {
                git url: 'https://github.com/shahar-re/cdex.git',
                branch: 'main',
                credentialsId: 'github_cred1'
            }
        }

        stage('Setting virtual environment'){
            steps{
                script{
                        sh """#!/bin/bash
                            python3 -m venv venv  # Create virtual environment
                            source venv/bin/activate  # Activate virtual environment
                        """
                }
            }
        }

        stage('Running the app'){
             steps{
                script{
                        sh """#!/bin/bash
                            source venv/bin/activate  # Activate virtual environment
                            python app.py  # Run the Python application
                        """
                }
             }
        }
    }

     post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
