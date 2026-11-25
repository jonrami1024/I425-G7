/*
Name: Angel Avila
Date: 11/25/26
File: build.jsx
Description:
*/

import {useEffect} from 'react';
import useAxios from '/src/hooks/useAxios';
import "/src/assets/css/build.css"
import {useParams, useOutletContext, Outlet} from "react-router-dom";

const Build = () => {
    const [, setSubHeading] = useOutletContext();
    const {buildId} = useParams();

    const {data: build, error, isLoading, abort, get}
        = useAxios("builds");

    useEffect(() => {
        if (buildId) {
            get(buildId);
        }

        // Abort request if component unmounts
        return () => {
            abort();
        };

        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [buildId]);

    // Set subheading once build is loaded
    useEffect(() => {
        if (build?.build_name) {
            setSubHeading(build.build_name);
        }

        return () => {
            setSubHeading("All Builds");
        };
    }, [build, setSubHeading]);

    return (
        <>
            {error && <div>{error}</div>}
            {isLoading &&
                <div className="image-loading">
                    Please wait while data is being loaded
                </div>}

            {build && <div className="build-details">
                <div className="build-info">
                    <div><strong>Name:</strong> {build.build_name}</div>
                    <div><strong>Build ID:</strong> {build.build_id}</div>
                    <div><strong>User ID:</strong> {build.user_id}</div>
                    <div><strong>Driver ID:</strong> {build.driver_id}</div>
                    <div><strong>Body ID:</strong> {build.body_id}</div>
                    <div><strong>Tire ID:</strong> {build.tire_id}</div>
                    <div><strong>Glider ID:</strong> {build.glider_id}</div>
                </div>
            </div>}

            {build && <div className="build-stats">
                <Outlet/>
            </div>}
        </>
    );
};

export default Build;