def deployRepoUrl = "https://$GIT_DEPLOY_KEY@github.com/Faithtosin/argocd-apps.git"
def cloneDir = "app-config"
def imageName = "public.ecr.aws/z1l0c6l7/simpleapp"

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

        stage('install dependencies') { 
            steps { 
                sh """
                 apt install make
                 curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash
                """
            }
        }
        // get git commit hash
        def scmInfo = checkout scm
        def gitCommit = "${scmInfo.GIT_COMMIT}"

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
        def env = "stage"
        stage('Deploy'){
            steps {
                withCredentials([file(credentialsId: 'githubDeployKey', variable: 'GIT_DEPLOY_KEY')]) {
                    sh """
                    git clone ${deployRepoUrl} cloneDir
                    cd cloneDir
                    export cloneDirFullPath=`pwd`
                    cd simpleapp-public/overlays/${env}
                    kustomize edit set image ${imageName}:${gitCommit}
                    cd ${cloneDirFullPath}
                    ./update-image.sh ${env} ${imageName} ${gitCommit}
                    """
                }
            }
        }
    }
}