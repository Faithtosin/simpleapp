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
                 docker build -t streamlit:${env.BUILD_NUMBER} .
                """
            }
        }
        stage('Test'){
            steps {
                sh """
                 docker run -d streamlit:${env.BUILD_NUMBER}
                """
            }
        }
        stage('Push'){
            steps {
                sh """
                 aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 698324764230.dkr.ecr.us-east-1.amazonaws.com && \
                 docker tag streamlit:${env.BUILD_NUMBER} 698324764230.dkr.ecr.us-east-1.amazonaws.com/streamlit-demo:${env.BUILD_NUMBER} && \
                 docker push 698324764230.dkr.ecr.us-east-1.amazonaws.com/streamlit-demo:${env.BUILD_NUMBER}
                """
            }
        }
    }
}