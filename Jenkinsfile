pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/karthikchapalamadugu/Assignment5'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x code.py"
                sh "./code.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Testforsub.py"
                sh "./Testforsub.py"
            }
        }
    } 
}
