import {
    CircularProgressbar,
    buildStyles
} from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

export function VolumeGauge({ volume }) {
    return (
        <div style={{ width: 100, height: 100 }}>
            <CircularProgressbar
                value={volume}
                text={`${volume}%`}
                styles={buildStyles({
                    pathColor: '#4ade80',
                    textColor: '#1f2937',
                })}
            />
        </div>
    );
}