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
        sh 'docker build -t $IMAGE_NAME -f Dockerfile_kpi .'
      }
    }

    stage('Test') {
      steps {
        echo 'Running tests...'
        sh 'pytest kpi_test_app.py'
      }
    }

    stage('Code Quality') {
      steps {
        echo 'Code quality analysis placeholder (e.g., SonarQube)...'
        // Example only: integration would go here
      }
    }

    stage('Security Scan') {
      steps {
        echo 'Running Trivy scan on Docker image...'
        sh 'trivy image $IMAGE_NAME || true'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying container...'
        sh '''
          docker rm -f $CONTAINER_NAME || true
          docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
        '''
      }
    }

    stage('Release') {
      steps {
        echo 'Creating release tag...'
        sh '''
          git config --global user.email "you@example.com"
          git config --global user.name "Wael Alahamdi"
          git tag -a v1.0 -m "First release"
          git push origin v1.0 || true
        '''
      }
    }

    stage('Monitoring') {
      steps {
        echo 'Simulating monitoring...'
        sh 'echo "Simulated metrics: container is running."'
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
