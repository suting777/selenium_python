pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: '71901886-3673-4bb3-a4a0-dcdacad0d7ea', branch: 'master', url: 'https://github.com/suting777/selenium_python.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
    steps {
        bat 'python selenium_python_ecommerce.py'
    }
}

    }
}
