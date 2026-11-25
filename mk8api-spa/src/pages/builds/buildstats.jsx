/*
Name: Angel Avila
Date: 11/25/26
File: buildstats.jsx
Description:
*/

import {useEffect} from 'react';
import useAxios from '/src/hooks/useAxios';
import {useParams} from "react-router-dom";
import "/src/assets/css/build.css"

const BuildStats = () => {

    const {buildId} = useParams();

    const {data: stats, error, isLoading, abort, get} = useAxios("builds");

    useEffect(() => {
        if (buildId) {
            get(`${buildId}/stats`)
        }

        // Abort request if component unmounts
        return () => {
            abort();
        };

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [buildId]);

    return (
        <>
            {error && <div>{error}</div>}
            {isLoading &&
                <div className="image-loading">
                    Please wait while data is being loaded
                </div>}

            {stats && <div className="build-stats">
                <h3>Build Parts</h3>

                <div><strong>Character:</strong> {stats.parts.driver}</div>
                <div><strong>Body:</strong> {stats.parts.body}</div>
                <div><strong>Tires:</strong> {stats.parts.tire}</div>
                <div><strong>Glider:</strong> {stats.parts.glider}</div>

                <br />
                <h3>Build Stats</h3>

                <div><strong>Speed:</strong> {stats.stats.speed.value}</div>
                <div><strong>Acceleration:</strong> {stats.stats.acceleration.value}</div>
                <div><strong>Weight:</strong> {stats.stats.weight.value}</div>
                <div><strong>Handling:</strong> {stats.stats.handling.value}</div>
                <div><strong>Traction:</strong> {stats.stats.traction.value}</div>
                <div><strong>Mini-Turbo:</strong> {stats.stats.mini_turbo.value}</div>
                <div><strong>Invincibility:</strong> {stats.stats.invincibility.value}</div>
            </div>}
        </>
    );
};

export default BuildStats;