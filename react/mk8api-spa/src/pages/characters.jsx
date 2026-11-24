/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: Characters.jsx
 * Description:
 */

import React from 'react';

const Characters = () => {
    return (
        <>
            <section className="content-box">
                <h2>Characters</h2>
                <hr/>
                <br/>
                <p>
                    {/* ill work on making this look more pretty - jonathan */}
                    There are 50 playable characters in Mario Kart 8 Deluxe, each with their own unique stats that
                    affect their performance on the track. <br/>
                    These stats include speed, acceleration, weight, handling, traction, and mini-turbo (hidden in
                    game). <br/>
                    The stats are divided into three categories: Small, Medium, and Large. Each category has its own
                    strengths and weaknesses.<br/>
                    For example small character have lower speed but higher handling and acceleration, while larger
                    characters have higher speed but lower handling and acceleration. <br/>
                </p>
            </section>
            <section>
                <h2> {/* Header */} </h2>
                <hr/>
                <br/>
            {/*  insert code here  */}
            </section>

        </>
    );
};

export default Characters;