pipeline {
    agent any
    options {
        timeout(time: 10, unit: 'MINUTES')  // Cancela el pipeline luego de 10 min.
        disableConcurrentBuilds()           // No permite ejecuciones paralelas del mismo job.
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo "Inicializando Construcción..."
                    sh 'bash scripts/build.sh'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo "Ejecutando Tests..."
                    sh 'bash scripts/test.sh'
                    echo 'Monitoreando Sistema...'
                    sh 'python3 scripts/monitor.py'
                }
            }
            post {
                always {
                    echo "Generando Reportes..."
                    //junit '**/test-reports/*.xml'
                }
            }
        }
        stage('Deploy(Simulación)') {
            steps {
                echo "Despegando entorno de prueba..."
                //sh 'scp bin/app user@server:/path'
            }
        }
    }
    post {
        success {
            echo "Pipeline Completado."
        }
        failure {
            echo "Pipeline Fallido. Verifica logs."
        }
    }
}