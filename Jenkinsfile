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
        bat "docker build -t %IMAGE_NAME% -f Dockerfile_kpi ."
      }
    }

    stage('Test') {
      steps {
        echo 'Running tests...'
        bat "docker run --rm -v %cd%:/app -w /app kpi-app pytest kpi_test_app.py"
      }
    }

    stage('Code Quality') {
      steps {
        echo 'Code quality analysis placeholder'
      }
    }

    stage('Security Scan') {
      steps {
        echo 'Simulated security scan (Trivy not installed)'
        bat 'echo No security scanner available'
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
        bat 'git config --global user.email "abubttalw@gmail.com"'
        bat 'git config --global user.name "Wael Alahamdi"'
        bat 'git tag -a v1.3 -m "Final release"'
        bat 'git push origin v1.3'
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
