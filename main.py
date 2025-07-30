from medical_data_visualizer import draw_cat_plot, draw_heat_map

if __name__ == "__main__":
    draw_cat_plot().savefig("catplot.png")
    draw_heat_map().savefig("heatmap.png")
    print(" Plots saved!")

