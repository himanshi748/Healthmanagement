pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'}
        }
        stage('Test') {
            steps {
                echo 'Testing..'}
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'}
        }
        stage('New Relic'){
           steps{
              script{
                  step([$class: 'NewRelicDeploymentNotifier', notifications: [[
                      apiKey: '4', 
                      applicationId: '', 
                      changelog: '', 
                      commit: '', 
                      deeplink: 'http://ceq-ict-laptop-161:8080/job/new%20relic%20two/configure', 
                      deploymentId: '', 
                      deploymentType: 'BASIC', 
                      description: '', 
                      entityGuid: 'MzYyNzM0NXxFWFR8U0VSVklDRXwtMjcxMTk0NzAyOTI0NzA1MTA2Mw',
                      groupId: '', 
                      revision: '', 
                      timestamp: '', 
                      user: 'himanshi.satpute@cloudeq.com', 
                      version: '1']]])
                   }
            }
        }
    }
}
