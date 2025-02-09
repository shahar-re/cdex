pipeline {
    agent {
        any
    }

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8-slim'  // Docker image to use
                    label 'docker'  // The label of the Jenkins agent that will run the container
                }
            }
            
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
