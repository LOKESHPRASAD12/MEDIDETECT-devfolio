import React from "react";
import { useNavigate } from "react-router-dom";
import {
    MDBBtn,
    MDBContainer,
    MDBRow,
    MDBCol,
    MDBCard,
    MDBCardBody,
    MDBInput,
  }
  from 'mdb-react-ui-kit';
  import 'mdb-react-ui-kit/dist/css/mdb.min.css';

function Login() {

    let navigate = useNavigate();

    const getLoginInfo=()=>{
        var email = document.getElementById("email").value;
        var pass = document.getElementById("pass").value;
        if(email==='clark134080@gmail.com' && pass==='easy'){
            navigate("/home")
        }
    }
    return(
        <MDBContainer fluid className='p-4 background-radial-gradient overflow-hidden' style={{height:900}}>

        <MDBRow>

        <MDBCol md='6' className='text-center text-md-start d-flex flex-column justify-content-center' style={{marginTop: 150}}>

            <h1 className="my-5 display-3 fw-bold ls-tight px-3" style={{color: 'hsl(218, 81%, 95%)'}}>
            MediDetect <br />
            <span style={{color: 'hsl(218, 81%, 75%)' }}>Medical Report Analysis using Image processing and NLP</span>
            </h1>

            <p className='px-3' style={{color: 'hsl(218, 81%, 85%)'}}>
            MediDetect is an advanced web application that combines AI-based image recognition and natural language processing (NLP) to analyze medical images (such as X-rays, CT scans) and medical reports, enabling doctors to detect diseases and assess the probability of certain conditions, leading to more precise diagnoses and effective treatment planning.          
            </p>

        </MDBCol>

        <MDBCol md='6' className='position-relative' style={{marginTop: 150}}>

            <div id="radius-shape-1" className="position-absolute rounded-circle shadow-5-strong"></div>
            <div id="radius-shape-2" className="position-absolute shadow-5-strong"></div>

            <MDBCard className='my-5 bg-glass'>
            <MDBCardBody className='p-5'>

                <MDBInput wrapperClass='mb-4' id="email" label='Email' type='email'/>
                <MDBInput wrapperClass='mb-4' id="pass" label='Password' type='password'/>
                <MDBBtn onClick={getLoginInfo} className='w-100 mb-4' size='md'>Log In</MDBBtn>

            </MDBCardBody>
            </MDBCard>

        </MDBCol>

        </MDBRow>

        </MDBContainer>
    )
}

export default Login;