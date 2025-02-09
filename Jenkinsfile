pipeline {
    agent any

    stages {
        stage('Checkout GitHub Repository') {
            steps {
                git url: 'https://github.com/shahar-re/cdex.git',
                branch: 'main',
                credentialsId: 'github_cred'
            }
        }
      
        stage('Install Python') {
            steps {
                script {
                    // Check if Python is installed, if not, install it
                        sh '''#!/bin/bash
                            if ! command -v python3 &>/dev/null; then
                                echo "Python3 not found, installing..."
                                sudo apt-get update
                                sudo apt-get install -y python3 python3-pip  # Install Python 3 and pip
                            else
                                echo "Python3 already installed"
                            fi
                        '''
                }
            }
        }

        stage('Setting virtual environment'){
                script{
                        sh '''#!/bin/bash
                                python3 -m venv venv  # Create virtual environment
                                source venv/bin/activate  # Activate virtual environment
                        '''
                }
        }

        stage('Running the app'){
                script{
                        sh '''#!/bin/bash
                                source venv/bin/activate  # Activate virtual environment
                                python app.py  # Run the Python application
                        '''
                }
        }
    }
}
