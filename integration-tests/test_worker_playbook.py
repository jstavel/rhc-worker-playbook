import pytest
import logging
import sh


def test_playbook_execution(not_registered_system, settings):
    logging.info(settings.env_for_dynaconf)
    sh.rhc('connect',
           '--username',settings.get('candlepin.username'),
           '--password',settings.get('candlepin.password'),
    )

    # wait for workers to load                                                                                                                                                                                                                
    #assert not os.path.exists(rhc_worker_test_file), "Test file exists when it shouldn't"                                                                                                                                                    

    #playbook_url = f"{application.rhc_client.config.sample_playbook_base_url}/{playbook}"                                                                                                                                                    
    #logger.info(f"Playbook will be downloaded from: {playbook_url}")                       
