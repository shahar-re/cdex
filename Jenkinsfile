pipeline {
    agent any

    stages {
        stage('Checkout GitHub Repository') {
            steps {
                git url: 'https://github.com/shahar-re/cdex.git',
                branch: 'main',
                credentialsId: 'github_cred1'
            }
        }
      
        stage('Install Python') {
            steps {
                script {
                    // Check if Python is installed, if not, install it
                        sh """#!/bin/bash
                            if ! command -v python3 &>/dev/null; then
                                echo "Python3 not found, installing..."
                                sudo apt-get update
                                sudo apt-get install -y python3  
                            else
                                echo "Python3 already installed"
                            fi
                        """
                }
            }
        }

        stage('Setting virtual environment'){
            steps{
                script{
                        sh """#!/bin/bash
                            sudo apt-get update
                            sudo apt install python3.12-venv
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
