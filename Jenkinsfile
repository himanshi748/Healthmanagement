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
                  step([$class: 'NewRelicDeploymentNotifier', notifications: [[apiKey: '${newrelic-api}', applicationId: '', changelog: '', commit: '', deeplink: '', deploymentId: '', deploymentType: 'BASIC', description: '', entityGuid: 'MzYyNzM0NXxFWFR8U0VSVklDRXwtMjcxMTk0NzAyOTI0NzA1MTA2Mw', european: false, groupId: '', revision: '', timestamp: '', user: 'himanshi.satpute@cloudeq.com', version: '1']]])
                   }
            }
        }
    }
}
