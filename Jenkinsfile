pipeline {
    agent any
    stages {
        
        stage('Checkout GitHub Repository') {
            agent {
                docker {
                    label 'docker'
                    image 'python:3.8'
                    args '-u root:root '
                }
            }

            steps {
                git url: 'https://github.com/shahar-re/cdex.git',
                branch: 'main',
                credentialsId: 'github_cred1'
            }
        }

       
        stage('Running the app'){
             agent {
                docker {
                    label 'docker'
                    image 'python:3.8'
                    args '-u root:root '
                }
            }

             steps{
                script{
                        sh """#!/bin/bash
                            
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
