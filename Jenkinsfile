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
                  step([$class: 'NewRelicDeploymentNotifier', notifications: [[apiKey: 'NRAK-OTDFMH5G2LAZE5VWOZ0WRBJ5TMA', applicationId: '1026772035', changelog: '', commit: '', deeplink: '', deploymentId: '', deploymentType: 'BASIC', description: '', entityGuid: 'MzYyNzM0NXxFWFR8U0VSVklDRXwtMjcxMTk0NzAyOTI0NzA1MTA2Mw', european: false, groupId: '', revision: '1', timestamp: '', user: 'himanshi.satpute@gmail.com', version: '1']]])
                   }
            }
        }
    }
}
