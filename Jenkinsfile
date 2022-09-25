pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    environment {
        cloneDir = 'app-config'
        imageName = 'public.ecr.aws/z1l0c6l7/simpleapp'
        scmInfo = checkout scm
        gitCommit = "${scmInfo.GIT_COMMIT}"
        ENV = "stage"
        deployRepoUrl = "https://${GIT_DEPLOY_KEY}@github.com/Faithtosin/argocd-apps.git"
    }
    stages {
         stage('Clone repository') { 
            steps { 
                script{
                checkout scm
                }
            }
        }
        
        stage('Build'){
            steps {
                withCredentials([[
                $class: 'AmazonWebServicesCredentialsBinding',
                credentialsId: "aws-credentials",
                accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]){
                sh """
                 export AWS_DEFAULT_REGION=us-east-1
                 aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/z1l0c6l7 && \
                 make publish
                """
                }
            }
        }
        stage('Deploy'){
            steps {
                withCredentials([string(credentialsId: 'githubDeployKey', variable: 'GIT_DEPLOY_KEY')]) {
                    sh """
                    rm -rf ${cloneDir}
                    git clone ${deployRepoUrl} ${cloneDir}
                    cd ${cloneDir}
                    
                    export cloneDirFullPath=`pwd`
                    cd simpleapp-public/overlays/${ENV}
                    kustomize edit set image ${imageName}:${gitCommit}
                    cd \$cloneDirFullPath
                    ./update-image.sh ${env} ${imageName} ${gitCommit}
                    """
                }
            }
        }
    }
}