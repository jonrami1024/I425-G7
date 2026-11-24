/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: nomatch.jsx
 * Description:
 */

import React from 'react';
import errorImage from '../assets/img/404.png';
const Nomatch = () => {
    return (
        <>
            <div className="main-heading">
                <img src={errorImage} alt="404 Error Image" className="error-image" width="250"/>
                <div className="container" className="error">Error</div>
            </div>
            <div className="sub-heading">
                <div className="container">404 Page Not Found</div>
            </div>
            <div className="main-content container" className="center">
                The page requested could not found. Please check your request and  try again.
            </div>
        </>
    );
};

export default Nomatch;