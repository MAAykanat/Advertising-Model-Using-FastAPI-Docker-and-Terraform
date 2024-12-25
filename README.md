# Table of Contents

   * [About Repo](#about-repo)
   * [Dataset](#dataset)
   * [Requirements](#requirements)
   * [How to use](#how-to-use)
   * [Authors](#authors)

# About Repo

    Well-know Advertising dataset is trained by using Random-Forest Regressor.
    
    Model deploy by using docker and terraform.

# Dataset

Link of dataset:

    https://github.com/erkansirin78/datasets/blob/master/Advertising.csv

# Requirements

    python==3.12.7
    fastapi[all]==0.115.5
    uvicorn[standard]==0.32.0
    pandas== 2.2.3
    scikit-learn==1.5.2
    sqlmodel==0.0.22
    pydantic[all]==2.10.0

# How to use 

    Model implemented on Windows, check for model saving location and method
    
    1. Train model
    
        python train_advertising.py

    2. Install Terraform

        sudo yum install -y yum-utils
        
        sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo

        sudo yum -y install terraform

        terraform --version
    
    3. Terraform Start

        terraform init

        terraform apply --auto-approve

        docker ps
    
    4. Check API on local

        http://localhost:8002/docs
    
    5. Terraform Destroy

        terraform destroy

# Author
    Muhammet Ali Aykanat

[![website](https://github.com/MAAykanat/MAAykanat/tree/d650e58697e2a74fc281eccacf19c5e46fbd89e2/img/linkedin.svg)](https://www.linkedin.com/in/muhammet-ali-aykanat/)