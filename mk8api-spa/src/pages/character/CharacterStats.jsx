/*
Name: Angel Avila
Date: 11/25/26
File: CharacterStats.jsx
Description:
*/

import {useEffect} from 'react';
import useAxios from '/src/hooks/useAxios';
import {useParams} from "react-router-dom";
import "/src/assets/css/character.css"

const CharacterStats = () => {

    const {driverId} = useParams();

    const {data: stats, error, isLoading, abort, get} = useAxios("drivers");

    useEffect(() => {
        if (driverId) {
            get(`${driverId}/stats`)
        }

        // Abort request if component unmounts
        return () => {
            abort();
        };

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [driverId]);

    return (
        <>
            {error && <div>{error}</div>}
            {isLoading &&
                <div className="image-loading">
                    Please wait while data is being loaded
                </div>}

            {stats && <div className="character-stats">
                <h3>Character Stats</h3>

                <div><strong>Group:</strong> {stats.label}</div>
                <div><strong>Size:</strong> {stats.size}</div>
                <div><strong>Speed:</strong> {stats.speed}</div>
                <div><strong>Acceleration:</strong> {stats.acceleration}</div>
                <div><strong>Weight:</strong> {stats.weight}</div>
                <div><strong>Handling:</strong> {stats.handling}</div>
                <div><strong>Traction:</strong> {stats.traction}</div>
                <div><strong>Mini-Turbo:</strong> {stats.mini_turbo}</div>
                <div><strong>Invincibility:</strong> {stats.invincibility}</div>
            </div>}
        </>
    );
};

export default CharacterStats;