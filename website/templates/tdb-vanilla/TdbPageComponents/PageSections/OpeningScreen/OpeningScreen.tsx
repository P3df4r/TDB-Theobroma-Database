import { useRef } from 'react';

import styles from './OpeningScreen.module.css';

import DatabaseIcon from '../../static/icons/database_icon.svg';

export default function OpeningScreen(){
  const openingScreen = useRef<HTMLDivElement>(null);

  setTimeout(()=>{
    if(openingScreen.current){
      openingScreen.current.style.opacity = '0';
    };
  }, 2500);

  setTimeout(()=>{
    if(openingScreen.current){
      openingScreen.current.style.display = 'none';
    };
  }, 3400);

  return(
    <div className={styles.container} ref={openingScreen}>
      <span className={styles.logo}>
        <figure>
          <img src={DatabaseIcon} alt="Database icon" />
        </figure>
        <span>TDB</span>
      </span>
    </div>
  );
};