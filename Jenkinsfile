pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
         stage('Clone repository') { 
            steps { 
                script{
                checkout scm
                }
            }
        }

        stage('Build') { 
            steps { 
                sh """
                 docker build -t streamlit:v1 .
                """
            }
        }
        stage('Test'){
            steps {
                sh """
                 docker run -rm streamlit:v1
                """
            }
        }
    }
}