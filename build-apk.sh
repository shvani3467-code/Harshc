name: Build Android APK with Briefcase

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Set up JDK 17
      uses: actions/setup-java@v4
      with:
        distribution: 'temurin'
        java-version: '17'

    - name: Install System Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip

    - name: Install Briefcase
      run: |
        python -m pip install --upgrade pip
        pip install briefcase

    - name: Create Briefcase Project
      run: briefcase create android --non-interactive

    - name: Build Android App
      run: briefcase build android --non-interactive

    - name: Package Android APK
      run: briefcase package android --non-interactive

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: briefcase-android-apk
        path: android/app/build/outputs/apk/debug/*.apk
        if-no-files-found: error
