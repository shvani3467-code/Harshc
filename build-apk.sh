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
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Set up JDK 17
      uses: actions/setup-java@v3
      with:
        distribution: 'temurin'
        java-version: '17'

    - name: Install Briefcase Dependencies
      run: |
        pip install --upgrade pip
        pip install briefcase

    - name: Create & Build Android App
      run: |
        briefcase create android --non-interactive
        briefcase build android --non-interactive
        briefcase package android --non-interactive

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v3
      with:
        name: briefcase-android-apk
        path: logs/**/*.apk # या android/gradle/app/build/outputs/apk/**/*.apk
