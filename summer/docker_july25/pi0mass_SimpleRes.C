#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include "TLorentzVector.h"
#include "TH1.h"

void pi0mass_SimpleRes(const char* filename) {
    // TFile* file1 = TFile::Open("GaussTuple_13142411.root");
    TFile* file1 = TFile::Open(filename);
    TDirectory* dir = file1->GetDirectory("DelphesTuple");
    TTree* rec_tree_i = (TTree*)dir->Get("SimpleRes");

    Long64_t eventNumber_i, eventNumber_t;
    //Double_t px_i, py_i, pz_i, eta_i, phi_i;
    //Double_t px_t, py_t, pz_t, eta_t, phi_t;
    //Double_t pt_i, pt_t;
    Double_t M, Mpi0 = 134.9770;
    Double_t Mmin = Mpi0 - 60.0, Mmax = Mpi0 + 60.0;
    Int_t pid_i, pid_t, mother_id_i, mother_id_t, mother_pid_i;

    Double_t p_i, p_t;
    Double_t xRec_i, yRec_i, zRec_i, xRec_t, yRec_t, zRec_t;
    Double_t xGen_i, yGen_i, zGen_i, xGen_t, yGen_t, zGen_t;
    Double_t px_i, py_i, pz_i, px_t, py_t, pz_t;

    //Double_t x_i, y_i, z_i, x_t, y_t, z_t;
    //Double_t theta, thetaX_i, thetaX_t, thetaY_i, thetaY_t;

    Double_t alpha = 0.1; // Default: 0.1
    Double_t beta = 0.01; // Default: 0.01

    Double_t factor = alpha*TMath::Sqrt(1000/(1+beta*beta));

    rec_tree_i->SetBranchAddress("eventNumber", &eventNumber_i);
    //rec_tree_i->SetBranchAddress("pxGen", &px_i);
    //rec_tree_i->SetBranchAddress("pyGen", &py_i);
    //rec_tree_i->SetBranchAddress("pzGen", &pz_i);
    //rec_tree_i->SetBranchAddress("eta", &eta_i);
    //rec_tree_i->SetBranchAddress("phi", &phi_i);
    rec_tree_i->SetBranchAddress("pidGen", &pid_i);
    rec_tree_i->SetBranchAddress("mother_ID", &mother_id_i);
    rec_tree_i->SetBranchAddress("mother_PID", &mother_pid_i);

    rec_tree_i->SetBranchAddress("pGen", &p_i);

    rec_tree_i->SetBranchAddress("xRec", &xRec_i);
    rec_tree_i->SetBranchAddress("yRec", &yRec_i);
    rec_tree_i->SetBranchAddress("zRec", &zRec_i);

    rec_tree_i->SetBranchAddress("xGen", &xGen_i);
    rec_tree_i->SetBranchAddress("yGen", &yGen_i);
    rec_tree_i->SetBranchAddress("zGen", &zGen_i);

    //rec_tree_i->SetBranchAddress("thetaX", &thetaX_i);
    //rec_tree_i->SetBranchAddress("thetaY", &thetaY_i);
    
    TCanvas *c1 = new TCanvas("c1", "c1");
    c1->cd();
    TH1F *hM = new TH1F("hM", "Inv. Mass histogram", 170, 50.0, 220.0); //40

    //TH1F *hE = new TH1F("hE", "Energy histogram", 100, 50.0, 20000.0);
    //TH1F *hEcorr = new TH1F("hEcorr", "Energy histogram", 100, 50.0, 20000.0);


    Double_t cos_theta;
    for (int i = 0; i < rec_tree_i->GetEntries(); ++i) {
        rec_tree_i->GetEntry(i);

        if (pid_i != 22 || mother_pid_i != 111) {
            continue;
        }

        eventNumber_t = eventNumber_i;
        mother_id_t = mother_id_i;

        //px_t = px_i;
        //py_t = py_i;
        //pz_t = pz_i;

        //eta_t = eta_i;
        //phi_t = phi_i;

        // p_i = gRandom->Gaus(1,beta) * gRandom->Gaus( p_i, factor*TMath::Sqrt(p_i) );

        //hE->Fill(p_i);
        //Double_t p_i_corr = gRandom->Gaus(1,beta) * gRandom->Gaus( p_i, factor*TMath::Sqrt(p_i) );
        // Double_t p_i_corr = 1000.0 * (gRandom->Gaus(1,beta) * gRandom->Gaus( 0.001 * p_i, factor*TMath::Sqrt(0.001 * p_i) ));
        //Double_t dE = p_i - p_i_corr;
        //std::cout << "p_i = " << p_i << "; p_i_corr = " << p_i_corr << "; dE = " << dE << '\n';
        // hEcorr->Fill(p_i_corr);
        // hE->Fill(dE);

        p_t = p_i;

        px_t = xRec_i - xGen_i;
        py_t = yRec_i - yGen_i;
        pz_t = zRec_i - zGen_i;

        // p_i = gRandom->Gaus(1,beta) * gRandom->Gaus( p_i, factor*TMath::Sqrt(p_i) );
        // p_t = gRandom->Gaus(1,beta) * gRandom->Gaus( p_t, factor*TMath::Sqrt(p_t) );
        //thetaX_t = atan(x_t / z_t);
        //thetaY_t = atan(y_t / z_t);
        //thetaX_t = thetaX_i;
        //thetaY_t = thetaY_i;
        // thetaX_t = tan(px_t / pz_t);
        // thetaY_t = tan(py_t / pz_t);
        //t = (12000.0 - z_i) / pz_i;
        //thetaX_t = atan((px_i * t) / (12000.0 - z_i));
        //thetaY_t = atan((py_i * t) / (12000.0 - z_i));

        for (int j = i + 1; j < rec_tree_i->GetEntries(); ++j) {
            rec_tree_i->GetEntry(j);
            if (eventNumber_i != eventNumber_t || pid_i != 22 || mother_id_i != mother_id_t || mother_pid_i != 111) {
                break;
            }

            //thetaX_i = atan(x_i / z_i);
            // thetaY_i = atan(y_i / z_i);
            // thetaX_i = atan(px_i / pz_i);
            // thetaY_i = atan(py_i / pz_i);

            //t = (12000.0 - z_i) / pz_i;
            //thetaX_i = atan((px_i * t) / (12000.0 - z_i));
            //thetaY_i = atan((py_i * t) / (12000.0 - z_i));

            // theta = sqrt((thetaX_i - thetaX_t) * (thetaX_i - thetaX_t) + (thetaY_i - thetaY_t) * (thetaY_i - thetaY_t));
            // M = sqrt(2.0 * p_i * p_t * (1.0 - cos(theta)));
            // p_i = p_i*1E-9;
            // p_i = 1000.0 * (gRandom->Gaus(1,beta) * gRandom->Gaus( 0.001 * p_i, factor*TMath::Sqrt(0.001 * p_i) ));
            // p_t = 1000.0 * (gRandom->Gaus(1,beta) * gRandom->Gaus( 0.001 * p_t, factor*TMath::Sqrt(0.001 * p_t) ));
            p_i = (gRandom->Gaus(1,beta) * gRandom->Gaus( p_i, factor*TMath::Sqrt(p_i) ));
            p_t = (gRandom->Gaus(1,beta) * gRandom->Gaus( p_t, factor*TMath::Sqrt(p_t) ));

            px_i = xRec_i - xGen_i;
            py_i = yRec_i - yGen_i;
            pz_i = zRec_i - zGen_i;

            cos_theta = ((px_t * px_i) + (py_t * py_i) + (pz_t * pz_i))
                / (
                    sqrt(px_t * px_t + py_t * py_t + pz_t * pz_t) 
                    * sqrt(px_i * px_i + py_i * py_i + pz_i * pz_i)
                   );

            M = sqrt(
                2 * p_t * p_i
                  * (1 - cos_theta)
            );


            //M = sqrt(
            //    (p_t + p_i) * (p_t + p_i) 
            //    - (px_t + px_i) * (px_t + px_i)
            //    - (py_t + py_i) * (py_t + py_i)
            //    - (pz_t + pz_i) * (pz_t + pz_i)
            //);

            // Inv. mass with gen info:
            // M = sqrt(
            //     (sqrt(px_t * px_t + py_t * py_t + pz_t * pz_t) + sqrt(px_i * px_i + py_i * py_i + pz_i * pz_i)) 
            //     * (sqrt(px_t * px_t + py_t * py_t + pz_t * pz_t) + sqrt(px_i * px_i + py_i * py_i + pz_i * pz_i))
            //     - (px_t + px_i) * (px_t + px_i)
            //     - (py_t + py_i) * (py_t + py_i)
            //     - (pz_t + pz_i) * (pz_t + pz_i)
            // );

            //if (M > Mmin && M < Mmax){
            hM->Fill(M);
            //}
        }
    }
  //hM->Draw();

  // hE->Draw();
  // hEcorr->Draw("same");
  ////TF1 *fit = new TF1("fit","gaus");
  //  TF1 *fit = new TF1("fit","crystalball");                                                                                                                                                                                                                                          
  //  (x, [Alpha], [N], [Sigma], [Mean])                                                                                                                                                                                                                                                
  //  fit->SetParameters(90, 134.97, 11.4, 1.9, 1.5);                                                                                                                                                                                                                                   
  ////hM->Fit(fit);

  gStyle->SetOptStat("emrou");
  hM->Draw();
  TF1 *fit = new TF1("fit", "gaus");
  hM->Fit(fit);
  gStyle->SetOptFit(1);

  FILE *fp = fopen("output_E.txt", "a+");
  if (fp != NULL) {
      //for (int i=0;i<fit->GetNpar();i++) {                           
    Float_t stddev = hM->GetStdDev();
    // Float_t rms = hM->GetRMS();
    Float_t sigma = fit->GetParameter(2);
    Float_t sigmaerr = fit->GetParError(2);
    fprintf(fp, "%s, %f, %f, %f\n", filename, stddev, sigma, sigmaerr);
      //}
  }
    
  fclose(fp);
}
