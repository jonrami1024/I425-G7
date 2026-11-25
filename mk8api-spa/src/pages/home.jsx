/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: home.jsx
 * Description:
 */

import React from 'react';

const Home = () => {
    return (
        <>
            <section className="content-box">
                <h2>Welcome to the Mario Kart 8 API</h2>
                <hr/>
                <br/>
                <p>
                    The Mario Kart 8 API is an unofficial, open-source utility that provides access to various data and
                    resources related to the popular racing game, Mario Kart 8.
                </p>
                <p>
                    The MK8 API contains all <a href="/driver/">driver</a>, <a href="/kart/">kart</a>, <a
                    href="/tire/">tire</a>, and <a href="/glider/">glider</a> stats, including speed, acceleration,
                    weight, handling, traction, and mini-turbo
                </p>
            </section>
            <section className="content-box">
                <h2>About the API</h2>
                <hr/>
                <br/>
                <p>
                    The MK8 Api is designed to provide developers and enthusiasts with easy access to the game's build
                    stats, allowing them to create their own applications, websites,
                    or tools that utilize this information.
                </p>
                <p>
                    One primary example example of this would be the <a href="/build-calculator/">build calculator</a>,
                    which allows users to input their desired character, kart, tire, and glider
                    combination and receive the resulting stats for that build. This can be useful for players who want
                    to optimize their builds for specific tracks or playstyles.
                </p>
            </section>
            <section className="content-box">
                <h2>Ready to Get Started?</h2>
                <hr/>
                <br/>
                <p>
                    To get started, click the Log In Button below. If you're new, Create an account.
                </p>
                <p>
                {/* Ill work on designing a proper button -jonathan */}
                    <a href="/login">Login</a>
                    {/*wym jsx doesnt like br tags*/}
                    <p></p>
                    <a href="/create-account">Create New Account</a>
                </p>
            </section>
        </>
    );
};

export default Home;