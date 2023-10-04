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
                  step([$class: 'NewRelicDeploymentNotifier', notifications: [[apiKey: '5b18b427-77dd-4d81-8a2d-9327825e949a', applicationId: '', changelog: '', commit: '', deeplink: '', deploymentId: '', deploymentType: 'BASIC', description: '', entityGuid: 'MzYyNzM0NXxBUE18QVBQTElDQVRJT058MTAyNjc3MjAzNQ', european: false, groupId: '', revision: '1', timestamp: '', user: 'himanshi.satpute@cloudeq.com', version: '1']]])
                   }
            }
        }
    }
}
