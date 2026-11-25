/*
Name: Angel Avila
Date: 11/25/26
File: character.jsx
Description:
*/

import {useEffect} from 'react';
import useAxios from '/src/hooks/useAxios';
import "/src/assets/css/character.css"
import settings from '/src/config/settings.jsx';
import {useParams, Link, useOutletContext, Outlet} from "react-router-dom";

const Character = () => {
    const [, setSubHeading] = useOutletContext();
    const {driverId} = useParams();

    const {data: character, error, isLoading, abort, get}
        = useAxios("drivers");

    useEffect(() => {
        if (driverId) {
            get(driverId);
        }

        // Abort request if component unmounts
        return () => {
            abort();
        };

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [driverId]);

    // Set subheading once character is loaded
    useEffect(() => {
        if (character?.name) {
            setSubHeading(character.name);
        }

        return () => {
            setSubHeading("All Characters");
        };
    }, [character, setSubHeading]);

    return (
        <>
            {error && <div>{error}</div>}
            {isLoading &&
                <div className="image-loading">
                    Please wait while data is being loaded
                </div>}

            {character && <div className="character-details">
                <div className="character-photo">
                    <img src={`${settings.baseApiUrl}/${settings.characterImageUrl}/${character.image_file}`}
                         alt={character.name}/>
                </div>

                <div className="character-info">
                    <div><strong>Name:</strong> {character.name}</div>
                    <div><strong>Driver ID:</strong> {character.driver_id}</div>
                    <div><strong>Driver Group ID:</strong> {character.driver_group_id}</div>
                </div>
            </div>}

            {character && <div className="character-stats">
                <Outlet/>
            </div>}
        </>
    );
};

export default Character;