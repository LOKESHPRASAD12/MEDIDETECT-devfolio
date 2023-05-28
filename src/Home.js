import React from "react";

function Home(){

    return(
        <div>
            <div class="row">
                <a href="/braintumor" class="col-4">
                    <h3 className="card_title">Brain Tumor</h3>
                </a>
                <a href="/brestcancer" class="col-4">
                    <h3 className="card_title">Breast Cancer</h3>
                </a>
                <a href="/cataract" class="col-4">
                    <h3 className="card_title">Cataract</h3>
                </a>
            </div>
            <div class="row">
                <a  href="/covid" class="col-4">
                    <h3 className="card_title">Covid</h3>
                </a>
                <a  href="/skin" class="col-4">
                    <h3 className="card_title">Skin</h3>
                </a>
                <a href="/reportannotation" class="col-4">
                    <h3 className="card_title">Report Annotation</h3>
                </a>
            </div>
        </div>
    )
}

export default Home;