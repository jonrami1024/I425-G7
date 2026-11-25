/**
 * Author: Jonathan Ramirez-Molina
 * Date: 11/24/2026
 * File: Characters.jsx
 * Description:
 */

import {useState, useEffect} from 'react';
import useAxios from '/src/hooks/useAxios';
import "/src/assets/css/character.css"
import {NavLink, Outlet} from "react-router-dom";

const Characters = () => {
    const [subHeading, setSubHeading] = useState("All Characters");

    const { data: characters, error, isLoading, abort, getAll } = useAxios('drivers');

    useEffect(() => {
        getAll();

        // Abort request if component unmounts
        return () => {
            abort();
        };

    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

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
                <br/>
                <div className="sub-heading">
                    <div className="container">{subHeading}</div>
                </div>
                <div className="main-content container">
                    {error && <div>{error}</div>}
                    {isLoading &&
                        <div className="image-loading">
                            Please wait while data is being loaded
                        </div>}

                    {characters && <div className="character-container">
                        <div className="character-list">
                            {characters.map((character) => (
                                <NavLink key={character.driver_id} to={`/characters/${character.driver_id}`}
                                         className={({isActive}) =>
                                             isActive ? "active" : ""}>
                                    <span>&nbsp;</span>
                                    <div>{character.name}</div>
                                </NavLink>
                            ))}
                        </div>
                        <div className="character-item">
                            <Outlet context={[subHeading, setSubHeading]} />
                        </div>
                    </div>}
                </div>
            </section>

        </>
    );
};

export default Characters;