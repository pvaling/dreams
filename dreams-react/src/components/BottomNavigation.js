import React from 'react';
import {makeStyles} from '@material-ui/core/styles';
import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
import RestoreIcon from '@material-ui/icons/Restore';
import FavoriteIcon from '@material-ui/icons/Favorite';
import LocationOnIcon from '@material-ui/icons/LocationOn';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';


function Feed() {
    return (
        <div>Feed</div>
    )
}
function MyDream() {
    return (
        <div>My Dream</div>
    )
}
function Stats() {
    return (
        <div>Stats</div>
    )
}

const useStyles = makeStyles({
    root: {
        width: 500,
    },
    stickToBottom: {
        width: '100%',
        position: 'fixed',
        bottom: 0,
    },
});

export default function SimpleBottomNavigation() {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);

    return (
        <BottomNavigation
            value={value}
            onChange={(event, newValue) => {
                setValue(newValue);
            }}
            showLabels
            className={[classes.root, classes.stickToBottom]}
        >
            <Router>
                <BottomNavigationAction component={Link} to="/feed" label="Feed" icon={<RestoreIcon/>}/>
                <BottomNavigationAction component={Link} to="/my-dream" label="My Dream" icon={<FavoriteIcon/>}/>
                <BottomNavigationAction component={Link} to="/stats" label="Stats" icon={<LocationOnIcon/>}/>

                <Route exact path="/" component={Feed}/>
                <Route path="/my-dream" component={MyDream}/>
                <Route path="/stats" component={Stats}/>

            </Router>
        </BottomNavigation>
    );
}
