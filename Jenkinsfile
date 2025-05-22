pipeline {
  agent any

  environment {
    IMAGE_NAME = 'kpi-app'
    CONTAINER_NAME = 'kpi-container'
  }

  stages {

    stage('Build') {
      steps {
        echo 'Building Docker image...'
        bat 'docker build -t $IMAGE_NAME -f Dockerfile_kpi .'
      }
    }

    stage('Test') {
      steps {
        echo 'Running tests...'
        bat 'pytest kpi_test_app.py'
      }
    }

    stage('Code Quality') {
      steps {
        echo 'Code quality analysis placeholder'
      }
    }

    stage('Security Scan') {
      steps {
        echo 'Running Trivy scan on Docker image...'
        bat 'trivy image $IMAGE_NAME || true'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying container...'
          bat "docker rm -f %CONTAINER_NAME%"
          bat "docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%"
      }
    }

    stage('Release') {
      steps {
        echo 'Creating release tag...'
          bat git config --global user.email "abubttalw@gmail.com"
          bat git config --global user.name "Wael Alahamdi"
          bat 'git tag -a v1.0 -m "First release"'
          bat git push origin v1.0 || true
      }
    }

    stage('Monitoring') {
      steps {
        echo 'Simulating monitoring...'
        bat 'echo "Simulated metrics: container is running."'
      }
    }
  }

  post {
    success {
      echo 'Pipeline completed successfully!'
    }
    failure {
      echo 'Pipeline failed. Check the logs.'
    }
  }
}
